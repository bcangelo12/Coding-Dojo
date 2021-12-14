select *
from users
left join tweets on users.id = tweets.user_id
where users.id = 1;

select tweets.tweet as kobe_tweets
from users
left join tweets on users.id = tweets.user_id
where users.id = 1;

SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 2;

select first_name, tweet
from users
left join faves
on users.id = faves.user_id
left join tweets
on faves.tweet_id = tweets.id
where users.id = 1 or users.id = 2;

select users.first_name as followed, users2.first_name as follower
from users
left join follows
on users.id = follows.followed_id
left join users as users2
on users2.id = follows.follower_id
where users.id = 1;